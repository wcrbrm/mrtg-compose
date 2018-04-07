# mrtg-compose
Command-line tool to compose MRTG configuration file

```
python mrtg-compose.py /etc/mrtg/mrtg.cfg init
python mrtg-compose.py /etc/mrtg/mrtg.cfg list 
python mrtg-compose.py /etc/mrtg/mrtg.cfg add disk xvda1
python mrtg-compose.py /etc/mrtg/mrtg.cfg remove disk
```

# to get exact numer of disk, run
# `snmptable -v2c -c public localhost diskIOTable`

```
AMAZON: xvda
DIGITAL OCEAN: vda
ARUBA: sda
```

