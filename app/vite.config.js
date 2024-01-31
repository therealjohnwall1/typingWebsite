import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: { //add for autoupdating
		watch:{
			usePolling: true
		}
	}
});
