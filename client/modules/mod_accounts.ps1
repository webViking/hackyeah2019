function mod-getUsers {
	return Get-LocalUser | Select-Object *;
}