function mod-getWindowsPatches {
	return get-wmiobject -class win32_quickfixengineering
}