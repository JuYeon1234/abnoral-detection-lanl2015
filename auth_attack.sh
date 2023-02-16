
while IFS='-' read -r f1 f2 f3 f4 f5 f6 f7
do
	 printf 'f1: %s, f2: %s, f3: %s f4: %s \n' "$f1" "$f2" "$f3" "$f4"
done < "./attack_log.csv"