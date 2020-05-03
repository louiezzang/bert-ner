# BERT-NER
This repository was forked and modified from
https://github.com/kamalkraj/BERT-NER-TF

## Fine tuning
### Pretrained models
Download Pretrained Models from Tensorflow offical models
* [bert-base-cased](https://storage.googleapis.com/cloud-tpu-checkpoints/bert/tf_20/cased_L-12_H-768_A-12.tar.gz) unzip into `cased_L-12_H-768_A-12`
* [bert-large-cased](https://storage.googleapis.com/cloud-tpu-checkpoints/bert/tf_20/cased_L-24_H-1024_A-16.tar.gz) unzip into `cased_L-24_H-1024_A-16`

### Run on Google Colab
See [bert_ner_colab.ipynb](https://github.com/louiezzang/bert-ner/blob/master/bert_ner_colab.ipynb)

How to prevent Google Colab from disconnecting:
* https://stackoverflow.com/questions/57113226/how-to-prevent-google-colab-from-disconnecting
* https://bryan7.tistory.com/1077
```js
function ClickConnect() {
    var buttons = document.querySelectorAll("colab-dialog.yes-no-dialog paper-button#cancel");
    buttons.forEach(function (btn) {
        btn.click();
    });
    console.log("Auto connect every 1 minute");
    document.querySelector("#top-toolbar > colab-connect-button").click();
}
setInterval(ClickConnect, 1000 * 60);
```

### Run on single GPU
```
python run_ner.py \
  --data_dir=data/ \
  --bert_model=cased_L-12_H-768_A-12 \
  --output_dir=out_base \
  --max_seq_length=128 \
  --do_train \
  --num_train_epochs 3 \
  --train_batch_size 32 \
  --do_eval \
  --eval_on dev
```

### Run on multi GPU
```
python run_ner.py \
    --data_dir=data/ \
    --bert_model=cased_L-24_H-1024_A-16 \
    --output_dir=out_large \
    --max_seq_length=128 \
    --do_train \
    --num_train_epochs 3 \
    --multi_gpu \
    --gpus 0,1,2,3 \
    --do_eval \
    --eval_on test
```

## Installation for serving
### Build docker image
```
docker build -t nextmining/bert-ner:latest .
```

### Run docker container
Run the docker container with interactive shell command mode.

```
docker stop bert-ner
docker rm bert-ner
docker run -i -t -v "$PWD:/app" --name bert-ner nextmining/bert-ner:latest /bin/bash
```
Enter the docker container with shell command.
```
docker exec -it YOUR_DOCKER_CONTAINER_NAME /bin/bash
docker exec -it bert-ner /bin/bash
```