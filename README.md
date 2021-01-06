0. find sequences on NCBI (I indcluded my search queries which seem to be returning correct results)
1. download sequences under dropdown menu (Send to: > Choose Destination = File > Format = FASTA CDS) look for "FASTA CDS" to download DNA coding sequences
2. concatenate all sequences in file to one entry using this online tool: https://www.bioinformatics.org/sms2/combine_fasta.html
3. copy output
4. paste output into codon usage calculator on https://www.bioinformatics.org/sms2/codon_usage.html
5. copy and paste codon usage output wherever you would like, I have included the input FASTA and the output results in this folder
6. I used a small python script to produce plots of all of the Codon Usage as you have demonstrated in the third slide of the powerpoint you sent over. you can check these against the chart, which is included in the textfile in this folder. script used to make these plots just takes data from the text output of the online codon usage calculator (just copy and pasted into a .txt) then it uses numpy and matplotlib libraries to generate graphics and render them as .png. script is in the folder as well