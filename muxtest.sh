#!/bin/bash

echo "##################"
echo "Beginning mux test"
echo "##################"

for val in {0..15}
do

   ./test_script.sh $val enable

   echo
   read -p "Hard drive boot done?(y) "
   echo
   if [[ $REPLY =~ ^[Yy]$ ]]
   then
      ./test_script.sh $val disable
   fi

   if [ $val = 15 ]
   then
      break
   fi

   echo
   echo "Now switch the hard drive inputs"
   read -p "Done?(y) "
   echo
   if [[ $REPLY =~ ^[Yy]$ ]]
   then
      continue
   fi

done
echo

echo "#####################"
echo "Done mux test, yay!!!"
echo "#####################"
