BEGIN {
    FS=","
    OFS="\t\t"
    OFMT="%.2f"
}
{
    #MIN[]
    #MAX[]

    if ($3 > MAX[$2]) {
        MAX[$2] = $3
    }
    if ($3 < MIN[$2]) {
        MIN[$2] = $3
    } else if (MIN[$2] == 0) {
        MIN[$2] = $3
    }

}
END {
    for (thing in MAX) {
        print thing,MAX[thing],MIN[thing]
    }
    print NR
}