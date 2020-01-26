<template>
  <div>
    <v-jsoneditor v-model="json" :options="options" :plus="false" height="400px" @error="onError"/>
    <v-btn color="primary" @click="submit">Submit</v-btn>
  </div>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'JsonEditor',
  data () {
    return {
      json: {},
      options: {
        mode: 'code'
      }
    }
  },
  created: function () {
    this.get()
  },
  methods: {
    async get () {
      var data = await $backend.getJson('test.json')
      this.json = data
    },
    async submit () {
      var data = await $backend.postJson('test.json', this.json)
      console.log(data)
    },
    onError () {
      console.log('error')
    }
  }
}
</script>
