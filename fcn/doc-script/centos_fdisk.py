# partiçoes
 
    ::: comandos para liostar as partiçoes do de disco

        $ fdisk -l
        $ sfdisk -l -uM
        $ parted -l
        
        $ df -h --output=source,fstype,size,used,avail,pcent,target -x tmpfs -x devtmpfs

        $ lsblk
        $ blkid