function mod-getAntivirusProduct {
	return Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct
}