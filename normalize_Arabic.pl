#!/usr/bin/perl

# 2017 QCRI Hassan Sajjad
# Partially borrowed from normalize script of Ahmed Ali

use warnings;
use strict;
use Encode;
use utf8;

# input an Arabic file and name of an output file
# normalize Arabic letters
# normalize Twitter related keywords
# lower case English


if (@ARGV !=2 )
    {#
	print "usage: $0 <inFile> <outFile>\n"; 
	exit (1);   
    }
    
my $inFile = shift (@ARGV);
my $outFile = shift(@ARGV);

open INFILE, "<$inFile" || die "unable to open the input file $inFile\n";
binmode INFILE, ":encoding(utf8)";

open OUTPUTFILE, ">$outFile" or die "unable to open the output mlf file $outFile\n";
binmode OUTPUTFILE, ":encoding(utf8)";

while (<INFILE>) {
  chomp;
  my $norm = normalize ($_);
  print OUTPUTFILE "$norm"."\n";
}
close INFILE;
close OUTPUTFILE;


sub normalize {

	my ($line)= $_;
	$line = lc $line;  # if english exists, lower case it
	$line =~ s/http\S*/\<url\>/g;   ## removing links
	$line =~ s/\@\S+/\<mention\>/g;    ## removing name mentions
	$line =~ s/RT //g;     ## removing any retweet shortcut in the text
	$line =~ s/rt //g;     ## removing any retweet shortcut in the text
	$line =~ s/[ًٌٍَُِّـْ]//g;     ## removing diacritics and kashidas
	$line =~ tr/أآإىة/ااايه/;    # normalizing standard Arabic characters
	$line =~ s/\#([^ ]+)/\<hash\>/g; # replace hash
	$line =~ s/\d+/ \<number\> /g;  # replace numbers with standard number tag
	$line =~ s/^\s*//; # remove leading spaces
	$line =~ s/\s*$//; # remove trailing spaces

#	$line =~ s/[_~=`#\^\-%&\*\+\|\{\}]//g; 
	
	## Remove Diacritics
	$line =~ s/\x{064B}//g;    ## FATHATAN
	$line =~ s/\x{064C}//g;    ## DAMMATAN
	$line =~ s/\x{064D}//g;    ## KASRATAN
	$line =~ s/\x{064E}//g;    ## FATHA
	$line =~ s/\x{064F}//g;    ## DAMMA
	$line =~ s/\x{0650}//g;    ## KASRA
	$line =~ s/\x{0651}//g;    ## SHADDA
	$line =~ s/\x{0652}//g;    ## SUKUN
	$line =~ s/\x{0670}//g;    ## SUPERSCRIPT ALEF
	$line =~ s/\x{0671}//g;    ## ALEF WASLA
	
	# Normalise the too many characters occurances to only 3 likr loooooool will be loool 
	$line =~ s/([^0-9])\1{2,}/$1$1$1/g;
	
    return $line;
}
