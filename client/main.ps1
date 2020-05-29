$ScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

$config = [pscustomobject]@{
	uri = "http://s2.msco.pl:8080/api/client/v1"
	uuid = "123"
	secret = "test"
}

try {
    . ("$ScriptDirectory\modules\mod_accounts.ps1")
    . ("$ScriptDirectory\modules\mod_antivirus.ps1")
    . ("$ScriptDirectory\modules\mod_apps.ps1")
    . ("$ScriptDirectory\modules\mod_firewall.ps1")
    . ("$ScriptDirectory\modules\mod_network.ps1")
    . ("$ScriptDirectory\modules\mod_patches.ps1")
    . ("$ScriptDirectory\modules\mod_services.ps1")
    . ("$ScriptDirectory\modules\mod_usblock.ps1")
	Write-Host "Data modules imported succesfully"
} catch {
    Write-Host "Error while loading Data modules." 
}

try {
    . ("$ScriptDirectory\lib_comm.ps1")
	Write-Host "Communication modules imported succesfully"
} catch {
    Write-Host "Error while loading Communication modules." 
}



$outputData = [pscustomobject]@{
	type 			= 'report'
	station_uuid  	= $config.uuid
	status			= $true
	data 			= [pscustomobject]@{
		apps 		= [pscustomobject]@{}
	}
}

Write-Progress -Activity "Gathering data" -status "User accounts" -percentComplete 0.0
$outputData.data | Add-Member -NotePropertyName accounts -NotePropertyValue (mod-getUsers)

# $outputData.data | Add-Member -NotePropertyName apps -NotePropertyValue [pscustomobject]@{}
Write-Progress -Activity "Gathering data" -status "Old apps" -percentComplete 20
$outputData.data.apps | Add-Member -NotePropertyName old -NotePropertyValue (mod-getOldApps)

Write-Progress -Activity "Gathering data" -status "Modern apps" -percentComplete 30
$outputData.data.apps | Add-Member -NotePropertyName modern -NotePropertyValue (mod-getModernApps)

Write-Progress -Activity "Gathering data" -status "Services" -percentComplete 35
$outputData.data | Add-Member -NotePropertyName services -NotePropertyValue (mod-getWindowsServices)

Write-Progress -Activity "Gathering data" -status "Antivirus products" -percentComplete 40
$outputData.data | Add-Member -NotePropertyName antivirus -NotePropertyValue (mod-getAntivirusProduct)

Write-Progress -Activity "Gathering data" -status "Firewall products" -percentComplete 60
$outputData.data | Add-Member -NotePropertyName firewall -NotePropertyValue (mod-getFirewallState)

Write-Progress -Activity "Gathering data" -status "Network adapters" -percentComplete 80
$outputData.data | Add-Member -NotePropertyName networkadapters -NotePropertyValue (mod-getNetworkAdapters)

Write-Progress -Activity "Gathering data" -status "Windows Update" -percentComplete 90
$outputData.data | Add-Member -NotePropertyName windowsupdate -NotePropertyValue (mod-getWindowsPatches)

Write-Progress -Activity "Gathering data" -status "USB Lock" -percentComplete 95
$outputData.data | Add-Member -NotePropertyName usblock -NotePropertyValue (mod-getUSBLock)

Write-Progress -Activity "Gathering data" -status "Done" -percentComplete 100


Write-Host "Sending data to host"

try {
	$token = libcomm-GetToken '123' 'test'
	Write-Host " - Authentication success"
} catch {
	Write-Host " - Failed to authenticate"
	# return;
}

try {
	$jsonData = $outputData | ConvertTo-Json
	Write-Host " - Prepared JSON"
} catch {
	Write-Host " - Failed to prepare JSON"
	return;
}

$result = libcomm-SendData 'x' $jsonData
try {
	Write-Host " - Sent data to server"
} catch {
	Write-Host " - Failed to sent data to server"
	return;
}

