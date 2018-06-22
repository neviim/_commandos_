#!/bin/bash
# cat /sys/class/net/enp1s0/statistics/tx_bytes
# cat /sys/class/net/enp1s0/statistics/rx_bytes
#
# ./net_velocidade_download.sk
#
 
while true; do # obviamente nunca sairá do loop, a não ser com um ctrl+c
	txInicial=`cat /sys/class/net/enp1s0/statistics/rx_bytes`
	sleep 1s
	txFinal=`cat /sys/class/net/enp1s0/statistics/rx_bytes`
	download=`echo $((($txFinal-$txInicial)/1024/1024)) | bc | awk '{printf "%.2f", $0}'` # medida em megabytes
	echo "$download kB/s"
done