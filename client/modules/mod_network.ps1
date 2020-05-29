function mod-getNetworkAdapters {
	# -IncludeHidden?
	return Get-NetAdapter -Name "*" #todo: custom (smaller) json
}