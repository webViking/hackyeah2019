function libcomm-GetToken([string]$uuid, [string]$password) {
	$jsonBody = [pscustomobject]@{
		uuid 		= $uuid
		password 	= $password
	} | ConvertTo-Json;
	
	$result = Invoke-WebRequest -Uri ($config.uri + "/auth")  -Method POST -Body $jsonBody;
	$result = $result | ConvertFrom-Json;
	
	if ($result.status){
		return $result.token;
	}

	return $false;
}

function libcomm-SendData([string]$token, [string]$JSONData) {
	Invoke-WebRequest -Uri ($config.uri + "/data") -Method POST -Headers @{"Authorization"=$token} -Body $JSONData  -ContentType "application/json; charset=utf-8";
	return $true;
}