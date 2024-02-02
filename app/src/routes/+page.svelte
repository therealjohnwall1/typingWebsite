<script>
	// Images
	import reload_img from "$lib/imgs/reset.png"
	import logo_img from "$lib/imgs/winton.jpg"
	import crown_img from "$lib/imgs/leaderboard.png"

	
	import { onMount } from 'svelte';
      // globs
    let WORD_AMT = 25;
    const back_domain = "http://localhost:8000";
    let word_promise;
	let word_bank;
    console.log("innitalizing word bank");

    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(WORD_AMT)
        word_promise = get_words(WORD_AMT)
		console.log("type: " + typeof word_promise);
		console.log("bank: " + word_promise);
    });

    function handle_keypress(event){
        pass
    }

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

	async function get_words_onclick(){
		await get_words();
	}
	function testStatus(){
		console.log(typeof word_bank);
	}

</script>

<svelte:head>
	<title> Typing Site</title>
</svelte:head>

<h1>
	<img src={logo_img} alt = "wynton"
	width = 35/>
	TypingTest
	<span>
	<button on:click = {get_words_onclick}>
		<img src={reload_img} alt="reload img"
		width = 30/>
	</button>
	<button>
		<img src={crown_img} alt="button for leaderboards" 
		width = 35/>
	</button>
		
	</span>
</h1>

<!-- <div>
	{#each word_bank as word}
		{#each word as letter}
			<letter> {letter} </letter>
		{/each}
	{/each}
</div> -->

<style>
	h1{
		color: rgb(139, 59, 59);
		font-family: 'Gotham';
		font-size: 1.75em;
		font-weight: 600;
	}

	

	:global(body) { 
		background-color: rgb(41, 35, 36);
  }
</style>