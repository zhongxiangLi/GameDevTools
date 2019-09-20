cd  /d  %~dp0

set GameDevTools_Python=%~dp0python-3.7.4-embed-amd64
set PATH=%PATH%;%GameDevTools_Python%

set GameDevTools_QtDepends=%~dp0python-3.7.4-embed-amd64\Tools\QtDepends
set PATH=%PATH%;%GameDevTools_QtDepends%

.\python-3.7.4-embed-amd64\GameDevTools.bat