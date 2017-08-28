Many researchers and developers use [the models that the fastText team has pre-trained on Wikipedia for hundreds of languages](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md).

### Downloading the models

The zipped models are on the order of 1GB to 10GB in size, depending on the size of the Wikipedia of the language, English being the largest.

To download pre-trained models for many languages into the current directory:

    wget https://raw.githubusercontent.com/SignalN/ftio/master/ftio/wiki/download.sh

    ./download.sh en ru zh es ar fr de it pt tr pl ja ko

If stopped it will not re-start automatically, but if re-started it will continue from where it stopped. 

Once finished, files `wiki.en.zip` ... `wiki.ko.zip` will be in the current directory.

To unzip them all:

    unzip \*.zip

If you run out of disk space when unzipping, remove .zip files that are already unzipped.

Once finished, directories `wiki.en/` ... `wiki.ko/` will be in the current directory, and inside each a `.bin` and `.vec`.


### Using the models

To use the models with a Python library like salestock/fasttext or Gensim that wraps or implements fastText:

    import ftio.wiki.preproc

    ... = preproc.line("This isn't a test!")


### About the models

Each text corpus was pre-processed with [get-wikimedia.sh](https://github.com/facebookresearch/fastText/blob/master/get-wikimedia.sh) before a model was trained with it.

In order to see the pre-trained trained models effectively, strings must be processed at runtime in the same way as the training data were pre-processed.

For example, there is no vector for `"Djibouti"`, only for `"djibouti"`.  Somewhat surprisingly, there are no vectors for `"1st"`, `"3d"`, `"don't"` or `"youtube.com"`.

The following pre-processing steps were taken on each line:
0. Lowercase
1. Remove wiki markup
2. Replace some punctuation with a space
3. Add a space around some other punctuation
4. Replace digits (0-9) with a space
5. Replace multiple spaces with a single space

`preproc.py` implements steps 0 and 2-5.
