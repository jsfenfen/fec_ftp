fec_ftp
=======

Another bucket of scripts/models for grabbing the fec's ftp data etc for django + postgres. Shell scripts for retrieving / moderately editing the raw files; sqlscripts for loading the data; django models so that the loaded data is available through django ORM. Sorta pointless, but dumped here for easier sharing. The paths are hardcoded in the sql scripts and will need to be set. Data directories--ie /ftpdata/data/YY/ will also need to be created, where YY = '12' for 2012, etc. 
