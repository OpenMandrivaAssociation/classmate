Name:		classmate
Version:	1.8.0
Release:	1
Summary:	Introspection of Java types with generic information
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/FasterXML/java-classmate
Source0:	https://github.com/FasterXML/java-classmate/archive/refs/tags/classmate-%{version}.tar.gz#/classmate-%{version}.tar.gz
BuildArch:	noarch
# The module descriptor is added by moditect, which is not packaged.
%global sysjar_drops --drop org.moditect:moditect-maven-plugin
BuildRequires:	python
BuildRequires:	mvn(com.fasterxml:oss-parent:pom::)
# oss-parent pins the compiler plugin's asm dependency at 9.11.1.
BuildRequires:	mvn(org.ow2.asm:asm)
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
ClassMate resolves field and method types, including generics.
1.8.0 is the current release and the one Jackson uses. It targets
Java 8. The OSGi bundle packaging is built as a plain jar.

%prep
%autosetup -n java-classmate-classmate-%{version}
python - <<'PY'
from pathlib import Path
p = Path("pom.xml")
text = p.read_text()
p.write_text(text.replace("<packaging>bundle</packaging>", "<packaging>jar</packaging>", 1))
PY

%files -f .mfiles
%doc LICENSE README.md
