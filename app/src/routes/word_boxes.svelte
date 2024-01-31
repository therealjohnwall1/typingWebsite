<script>
    import { onMount } from 'svelte';
    import main_words from '$lib/words/top1kwords.txt';
  
    let lines = [];
    let word_file_lines = 10000;
    let word_amount = 25;

  
  // take user input -> # of characters intered = letter tag 
  //update from there
    onMount(async () => {
      console.log(`Mounting to DOM`)
      
      lines = get_words(main_words);

      // document.addEventListener('click', onClickDocument, {
			// capture: true});

    });
    function get_words(path){
      
      const fileInput = document.getElementsByID(path);

      let lines = text.split('\n');
      let index = 0;
      let prompt = [];
      for(let i = 0; i< word_amount;i++){
        index = Math.random() * (word_file_lines);
        prompt += lines[index];
        prompt += " ";
      }
      console.log(prompt);
      return prompt;
      
    }

    const add_string = (word) => {word_string += word; return word_string}
    const reset = () => {word_string = ""; return ""}

    function handle_keydown(event) {
      const keyPressed = event.key;
      console.log(`User input:${keyPressed}`)
      userInput += keyPressed;
      updateWordStyles();
    }

    // Add event listener to capture keydown events
  function updateWordStyles() {
    // Update the styles based on userInput
    lines = lines.map(word => ({
      original: word,
      styled: applyStyles(word),
    }));
  }
  function applyStyles(word) {
    const matchedLetters = word
      .split('')
      .map((letter, index) => {
        if (index < userInput.length) {
          return userInput[index] === letter ? 'green' : '';
        }
        return '';
      });

    return matchedLetters.join(' ');
  }


  $: word_string = "";

  let user_input = "";
    
</script>
  

<!-- <svelte:body on:focus={}/> -->



<!-- svelte-ignore a11y-no-static-element-interactions -->

<div class="word-box" class:loading={!lines.length} on:keydown={handle_keydown} tabindex=-1>
    {#each lines as word,index}
      <div class="word 21savage">
        {#each word as letter}
        <letter class = {index}>
          {letter}
        </letter>
        {/each}
      </div>
      <!-- <br> -->
    {/each}
    {#if !lines.length}Loading{/if}
</div>


<!-- <label>
  <input bind:value={user_input}>
</label> -->

  <style>
    .word-box {
      display: flex;
      flex-wrap: wrap;
      flex-direction: row;
      justify-content: space-around;
      /* ... other styles ... */
    }
    .word{
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        font-size: xx-large;

    }
 
  
  
    .loading {
      opacity: 0.3;
    }
  </style>
  