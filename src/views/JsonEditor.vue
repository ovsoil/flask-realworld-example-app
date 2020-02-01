<template>
  <div align=middle>
    <v-flex xs11>
      <v-jsoneditor v-model="json" :options="options" :plus="false" height="400px" @error="onError"/>
      <v-btn color="primary" @click="submit">Submit</v-btn>
    </v-flex>
  </div>
</template>

<script>
import VJsoneditor from 'v-jsoneditor'
import $backend from '../backend'

export default {
  name: 'JsonEditor',
  components: {
    VJsoneditor
  },
  data () {
    return {
      json: {},
      options: {
        mode: 'code'
      }
    }
  },
  mounted () {
    this.get()
  },
  methods: {
    async get () {
      var data = await $backend.getJson('data-basic.json')
      this.json = data
    },
    async submit () {
      var data = await $backend.postJson('data-basic.json', this.json)
      console.log(data)
    },
    onError () {
      console.log('error')
    }
  }
}
</script>

<style lang="scss">
.ace_gutter {
  z-index: 1;
}
</style>
