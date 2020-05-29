Function Test-RegistryValue {
	param
	(
		[Object]
		$regkey,

		[Object]
		$name
	)

	$exists = Get-ItemProperty -Path "$regkey" -Name "$name" -ErrorAction SilentlyContinue
	If (($exists -ne $null) -and ($exists.Length -ne 0)) {
		Return Write-Host 'The policy is Enabled...' -BackgroundColor Green -ForegroundColor Black
	}
	Return Write-Host 'The policy is Disabled...' -BackgroundColor Green -ForegroundColor Black
}

function mod-getUSBLock {
	return Test-RegistryValue -regkey 'HKLM:\Software\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}' -Name 'Deny_Read'
}