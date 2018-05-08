#!//bin/bash
for i in ../*/*py
do
    grep ^import $i | sed 's/import //g'
done
