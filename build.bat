@echo off
setlocal enabledelayedexpansion
set "JAVA_HOME=C:\Program Files\Microsoft\jdk-21.0.11.10-hotspot"
cd /d "c:\Users\Admin\Desktop\Java"
"C:\apache-maven-3.9.16\bin\mvn.cmd" clean test-compile 2>&1
