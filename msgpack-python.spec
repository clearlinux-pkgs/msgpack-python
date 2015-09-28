#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msgpack-python
Version  : 0.4.6
Release  : 14
URL      : https://pypi.python.org/packages/source/m/msgpack-python/msgpack-python-0.4.6.tar.gz
Source0  : https://pypi.python.org/packages/source/m/msgpack-python/msgpack-python-0.4.6.tar.gz
Summary  : MessagePack (de)serializer.
Group    : Development/Tools
License  : Apache-2.0
Requires: msgpack-python-python
BuildRequires : msgpack-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======================
MessagePack for Python
=======================
:author: INADA Naoki
:version: 0.4.5
:date: 2015-01-25

%package python
Summary: python components for the msgpack-python package.
Group: Default

%description python
python components for the msgpack-python package.


%prep
%setup -q -n msgpack-python-0.4.6

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test-2.7
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
