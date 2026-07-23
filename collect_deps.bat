@echo off
setlocal enabledelayedexpansion
set "JAVA_HOME=C:\Program Files\Microsoft\jdk-21.0.11.10-hotspot"
cd /d "c:\Users\Admin\Desktop\Java"
"C:\apache-maven-3.9.16\bin\mvn.cmd" dependency:list -DoutputAbsoluteArtifactId=true > ".github\modernize\java-upgrade\20260706123137\deps_raw.txt" 2>&1
findstr "[INFO]" ".github\modernize\java-upgrade\20260706123137\deps_raw.txt" | findstr ":" > ".github\modernize\java-upgrade\20260706123137\deps.txt"
type ".github\modernize\java-upgrade\20260706123137\deps.txt"
