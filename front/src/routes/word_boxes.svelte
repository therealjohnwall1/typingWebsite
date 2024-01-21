<script>
    import { onMount } from 'svelte';
    import main_words from '$lib/words/top1kwords.txt';
  
    let lines = []; // Reactive variable
  
    onMount(async () => {
      const text = await fetch(main_words).then(res => res.text());
      lines = text.split('\n');
    });
  </script>
  
  
  <div class="word-box" class:loading={!lines.length}>
    {#each lines.slice(0, 25).sort(() => Math.random() - 0.5) as word}
      <div class="word">{word}</div>
    {/each}
    {#if !lines.length}Brrrr...{/if}
  </div>
  
  <style>
    .word-box {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      /* ... other styles ... */
    }
    /* .word{
        
    } */
  
  
    .loading {
      opacity: 0.3;
    }
  </style>
  