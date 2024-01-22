<script>
    import { onMount } from 'svelte';
    import main_words from '$lib/words/top1kwords.txt';
  
    let lines = [];
    let word_file_lines = 10000;
    let word_amount = 25;
  
    let word_string = ""; 
  
  // take user input -> # of characters intered = letter tag 
  //update from there
    onMount(async () => {
      const text = await fetch(main_words).then(res => res.text());
      lines = text.split('\n');
      
    });

    const add_string = (word) => {word_string += word; return word_string}
    const reset = () => {word_string = ""; return ""}

    function handle_keydown(event) {
      const keyPressed = event.key;
      userInput += keyPressed;
      updateWordStyles();
  }
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
    
</script>
  
  
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="word-box" class:loading={!lines.length} on:keydown={handle_keydown} tabindex=-1>
    {#each lines.slice(0, 25).sort(() => Math.random() - 0.5) as word}
      <div class="word">
        {#each word as letter}
        <letter class = {letter}>
          {letter}
        </letter>
        {/each}
      </div>
    {/each}
    {#if !lines.length}Brrrr...{/if}
</div>

  
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
  