def check_text(text):
    text_splitted =[chr for chr in text]
    count =0
    redundant_chr_count=0

    for chr in text_splitted:
        try:
            prev_chr= text_plitted[text_splitted.index(chr)-1]
        except IndexError:
            prev_chr = None

            if prev_chr == chr:
                del text_splitted[count]
                redundant_chr_count+=1
                count -=1
                count +=1

                return text_splitted.join(''),
            redundant_chr_count
