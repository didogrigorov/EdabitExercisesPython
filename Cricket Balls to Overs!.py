def total_overs(balls):

    result = divmod(balls, 6)
    final = [str(x) for x in result]

    if final[1] == "0":
        return final[0]
    else:
        result = '.'.join(final)
        final = float(result)
        return final

print(total_overs(164))