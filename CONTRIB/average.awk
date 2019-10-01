BEGIN {
    FS=","
    OFS="\t\t"
    OFMT="%.2f"
}
{
    HP_SUM[$2] += $3
    COUNT[$2]++
    ATTACK_SUM[$2] += $4
}
END {
    for (thing in HP_SUM) {
        print thing,HP_SUM[thing]/COUNT[thing],ATTACK_SUM[thing]/COUNT[thing]
    }
    print NR
}