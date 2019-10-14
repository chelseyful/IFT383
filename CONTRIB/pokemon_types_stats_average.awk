BEGIN {
    FS=","
    OFS="\t"
    OFMT="%.2f"
}
$3~/[0-9]+/ {
    HP_SUM[$2] += $3
    ATTACK_SUM[$2] += $4
    COUNT[$2]++
}
END {
    for (thing in HP_SUM) {
        print thing,HP_SUM[thing]/COUNT[thing],ATTACK_SUM[thing]/COUNT[thing]
    }
}