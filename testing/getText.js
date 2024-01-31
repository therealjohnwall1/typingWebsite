const fs = require('fs');

let path = 'top1kwords.txt';
lines = get_words(path);


function get_words(path) {
  word_amount = 25;
  word_file_lines = 10000;
  fs.readFile(path, (err, inputD) => {
    if (err) throw err;
    let text = inputD.toString();
    console.log(text);

    let lines = text.split('\n');
    let index = 0;
    let prompt = [];
    for (let i = 0; i < word_amount; i++) {
      index = Math.random() * word_file_lines;
      prompt += lines[index];
      prompt += " ";
    }
    console.log(prompt);
    return prompt;
  });
}
