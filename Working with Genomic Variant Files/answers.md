## Answers to questions from "Genomic Variant Files"

**Q1: How many positions are found in this region in the VCF file?**

A: There were 69 positions found in that region within the VCF file. This was found with the following command:
```shell
tabix CEU.exon.2010_03.genotypes.vcf.gz 1:1105411-44137860 | wc -l
```

**Q2: How many samples are included in the VCF file?**

A: There were 90 samples in the VCF file. This was found with the following command: 
```shell
bcftools query -l CEU.exon.2010_03.genotypes.vcf.gz | wc -l
```

**Q3: How many positions are there total in the VCF file?**

A: There were 3489 total positions in the VCF file. This was found with the following command: 
```shell
bcftools query -f '%POS\n' CEU.exon.2010_03.genotypes.vcf.gz | wc -l
```

**Q4: How many positions are there with AC=1? Note that you cannot simply count lines since the output of bcftools filter includes the VCF header lines. You will need to use bcftools query to get this number.**

A: There were 1075 positions where the allele count was one. This was found with the following command:
```shell
bcftools query -f '%POS\n' -i AC=1 CEU.exon.2010_03.genotypes.vcf.gz | wc -l
```

**Q5: What is the ratio of transitions to transversions (ts/tv) in this file?**

The ts/tv ratio was 3.47.

**Q6: What is the median number of variants per sample in this data set?**

The median number of variants per sample was 28.