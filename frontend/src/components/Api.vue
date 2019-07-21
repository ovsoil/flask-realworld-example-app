<template>
  <div class="about">
    <h1>Call Backend API Demo</h1>
    <p>Click on the links below to fetch data from the Flask server</p>
    <a href="" @click.prevent="fetchRandom">Fetch Random</a>
    <a href="" @click.prevent="clearCache">Clear Cache</a><br/>
    <h4>Results</h4>
    <p v-for="(r, i) in resources" :key="i">
      <a> Data: {{r.data}}</a>
      <a> Time: {{r.timestamp | formatTimestamp }}</a>
    </p>
    <p>{{info}}</p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: [],
      info: ''
    }
  },
  methods: {
    async fetchRandom () {
      try {
        var data = await $backend.fetchRandomResource()
        this.resources.push(data)
      } catch (error) {
        this.info = error.message
      }
    },

    async clearCache () {
      try {
        var data = await $backend.clearRandomCache()
        this.info = data.data ? 'cache cleared' : 'no cache'
      } catch (error) {
        this.info = error.message
      }
    }
  }
}

</script>

<!-- <style lang="scss"> -->
<!-- </style> -->
