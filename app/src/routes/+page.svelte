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
	let word_correct; 

    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(WORD_AMT)
        word_promise = get_words(WORD_AMT)
		console.log("type: " + typeof word_promise);
		console.log("bank: " + word_promise);
		wordContainer.focus();
    });


	let clear;
	let seconds = 0; //measured in seconds 
	function increment(){
		seconds+=1;
	}

	$:{
		clearInterval(clear);
		clear = setInterval(increment, seconds);
	}


	// pulling data for words
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

	//make sure to add spaces between the words when typing 
	function keyDown(event){		
		let currentWord = word_bank[caretIndex.word];
		let currentChar = currentWord[currentWord.length - 1];

		if(caretIndex.word === 0 && caretIndex.letter == 0){
			//timer start 
		}
		if (event.key === 'Backspace' || event.key === 'Delete'){
			caretIndex.letter--;
				if(caretIndex.letter === 0){
					caretIndex.word--;
					caretIndex.letter = word_bank[caretIndex.word].length;
				}
		}
		
		else{
			if(event.key === currentChar){
				console.log("it should be moving");
				//set it to green
			}
			else{
				//set it to red
			}
			caretIndex.letter++;
			if(caretIndex.letter === currentWord.length){
				console.log(caretIndex);
				caretIndex.word++;
				caretIndex.letter = 0;
			}
		}

	}

	//changing word amt in query
	function changeWords(amt){
		WORD_AMT = amt;
		resetWords();
	}


	function calcWpm(time){
		return WORD_AMT/time;
	}

</script>

<svelte:head>
	<title> Typing Site idk</title>
</svelte:head>

<input type = 'number' bind:value = {seconds}>

<h1>
	<span>
	<button >
		<img src={crown_img} alt="button for leaderboards" 
		width = 35/>
	</button>
	<button on:click = {testStatus}>
		testing
	</button>
	</span>
</h1>

<h3 class = "query_settings">
	<span>
		<button class = "change_words" on:click={changeWords(15)}>
			15
		</button>

		<button class = "change_words" on:click={changeWords(25)}>
			25
		</button>

		<button class = "change_words" on:click={changeWords(50)}>
			50
		</button>

		<button class = "change_words" on:click={changeWords(100)}>
			100
		</button>
	</span>
</h3>

<!-- add autofocus onto button and change the color to more natural -->
<button class="word-container" bind:this ={wordContainer} on:keydown={keyDown}>
		{#each word_bank as word, i}
			<div class="word">
				{#each word as letter, j}
				{#if i === caretIndex.word && caretIndex.letter === j }
					<letter class = "selectedLetter">
						<span style="display: inline-block; border-right: padding-right: 100px; color: yellow; font-weight: bold; height: 20px;">|
						</span>{letter}

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
		color: #3500D3;
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
		/* color: #12343b; */
		background-color: #282828;
		padding: 0;
		border: #282828;

		
		 /* Change the background color to your desired color */
	}

	.change_words{
		background-color: #5930d3;
		border: #282828;
	}
	.word {
		font-size: 3em;
		font-weight: 450;
		margin-right: 10px;
		margin-bottom: 10px;
		color: #5930d3;
		font-family: 'Gotham';
	}
	.correct{
		color:#e1b382
	}
	.incorrect{
		color:#c22a2a
	}
	.selectedLetter {
		/* background-color: rgb(252, 252, 252); */
		border-radius: 20px;
	}  


	:global(body) { 
		background-color: #282828;
  }
</style>