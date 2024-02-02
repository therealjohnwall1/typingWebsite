<script>
	// Images
	import reload_img from "$lib/imgs/reset.png"
	import crown_img from "$lib/imgs/leaderboard.png"
	import test from "$lib/imgs/favicon.png"

	
	import { onMount } from 'svelte';
      // globs
	console.log("innitalizing word bank");
	let WORD_AMT = 25;
    const back_domain = "http://localhost:8000";
    let word_promise;
	let word_bank = [];
	let wordContainer;
	let caretIndex = {
		word:0,
		letter:0
	};



    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(WORD_AMT)
        word_promise = get_words(WORD_AMT)
		console.log("type: " + typeof word_promise);
		console.log("bank: " + word_promise);
		wordContainer.focus();
    });

	//watch promise tutorial on yt
    async function get_words(){
        const params = {
            size: WORD_AMT
        };

		let word_data;
        const queryString = Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
       
        const url = `${back_domain}/getWords?${queryString}`;

        fetch(url)
            .then(response => {
            if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
            }
            return response.json();
            })
            .then(data => {
			word_bank = data;
            console.log("works: " + word_bank);
			console.log("type: " + typeof word_bank);
            })
            .catch(error => {
            console.error('Error:', error);
            });
    }

	async function resetWords(){
		await get_words();
		caretIndex = {word:0, letter:0};
	}
	function testStatus(){
		console.log(word_bank);
		console.log(typeof word_bank);
	}

	// event listeners
	function keyDown(event){
		console.log(event.key); 
		// const currWord = word_bank[caretIndex.word];
		
		let currentWord = word_bank[caretIndex.word] 
		if (currentWord) {
			const typedChar = event.key.toLowerCase();
			const currentChar = currentWord[currentWord.length - 1].toLowerCase();

			if (typedChar === currentChar) {
				caretIndex.letter++;
			}
			if (caretIndex.letter >= currentWord.length) {
				caretIndex.letter = 0;
				currentWord++;
				// next word
			}
    	}
	}

	// document.addEventListener('keydown', keyDown);
	
	function handleKeyDown(event) {
    if (event.key.length === 1) {
      // Only handle single character keys (letters, numbers, etc.)
      const pressedLetter = event.key.toUpperCase();

      const currentWord = word_bank[caretIndex.word];
      const currentLetter = currentWord[caretIndex.letter];

      if (pressedLetter === currentLetter) {
        // Handle correct key press
        console.log('Correct key pressed!');
        caretIndex.letter++;

        if (caretIndex.letter >= currentWord.length) {
          // Move to the next word when reaching the end of the current word
          caretIndex.word++;
          caretIndex.letter = 0;
        }
		// Add logic for when all words are completed
        if (caretIndex.word >= word_bank.length) {
          console.log('All words completed!');
          // Reset the caretIndex or perform other actions as needed
        }
      } else {
        // Handle incorrect key press
        console.log('Incorrect key pressed!');
        // Add logic for incorrect input if needed
      }
    }
  }

</script>

<svelte:head>
	<title> Typing Site idk</title>
</svelte:head>

<h1>
	<span>
	<button>
		<img src={crown_img} alt="button for leaderboards" 
		width = 35/>
	</button>
	<button on:click = {testStatus}>
		testing
	</button>
	</span>
</h1>


<button class="word-container" bind:this ={wordContainer} on:keydown={keyDown}>
		{#each word_bank as word, i}
			<div class="word">
				{#each word as letter, j}
				{#if i === caretIndex.word && caretIndex.letter === j }
					<letter class = "selectedLetter">
						<span style="display: inline-block; border-right: padding-right: 100px; color: yellow; font-weight: bold; height: 20px;">|</span>{letter}
					</letter>
				{:else}	
					<letter>
						{letter}
					</letter>
					{/if}
				{/each}
			</div>
		{/each}
</button>

<div class = "reload">
	<button on:click = {resetWords}>
		<img src = {reload_img} alt = "button to reset words"
		width = 80>
		
	</button>
</div>


<style>
	h1{
		color: #FAD5A5;
		font-family: 'Gotham';
		font-size: 3em;
		font-weight: 600;
	}
	.reload {
		display: flex;
		justify-content: center;
		align-items: center;
		opacity: 0.5;
		margin-right: auto;
		margin-left: auto;
	}
	.word-container {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
		margin-right: 170px;
		margin-left: 170px; 
	}

	.word {
		font-size: 2.15em;
		font-weight: 450;
		margin-right: 10px;
		margin-bottom: 10px;
		color: #e1b382;
		font-family: 'Gotham';
	}
	.correct{
		color:#e1b382
	}
	.incorrect{
		color:#c22a2a
	}
	.selectedLetter {
		/* background-color: rgb(110, 214, 133);
		border-radius: 20px;
		 */
	}

	

	:global(body) { 
		background-color: #12343b;
  }
</style>