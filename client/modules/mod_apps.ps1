function mod-getOldApps {
	return Get-WmiObject -Class Win32_Product
}
function mod-getModernApps {
	return Get-AppxPackage -AllUsers | Select-Object *
}