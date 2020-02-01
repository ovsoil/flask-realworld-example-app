<template>
  <v-container fluid grid-list-md>
  <v-layout row>
    <v-flex xs6>
      <v-form v-model="formValid">
        <v-jsonschema-form v-if="schema" :schema="schema" :model="dataObject" :options="options" @error="showError" @change="showChange" @input="showInput" />
      </v-form>
    </v-flex>
    <v-flex xs6 id="json">
      <h2 class="title my-4">
        Data:
      </h2>
      <pre>{{ JSON.stringify(dataObject, null, 2) }}</pre>
    </v-flex>
  </v-layout>
  </v-container>
</template>

<script>
import $backend from '../backend'
import VJsonschemaForm from '@koumoul/vuetify-jsonschema-form/lib/index.vue'

export default {
  name: 'JsonForm',
  components: { VJsonschemaForm },
  data () {
    return {
      schema: null,
      schemaError: null,
      dataObject: {},
      formValid: false,
      options: null
    }
  },
  mounted () {
    this.Load()
  },
  methods: {
    async Load () {
      const data = await $backend.getJson('data-basic.json')
      const schema = await $backend.getJson('schema-basic.json')
      console.log(data)
      console.log(schema)

      this.schemaError = null
      this.options = {
        debug: true,
        disableAll: false,
        autoFoldObjects: true,
        context: { owner: { type: 'organization', id: '5a5dc47163ebd4a6f438589b' } },
        accordionMode: 'normal'
      }
      this.dataObject = data
      this.schema = schema
    },
    showError (err) {
      window.alert(err)
    },
    showChange (e) {
      console.log('"change" event', e)
    },
    showInput (e) {
      console.log('"input" event', e)
    }
  }
}
</script>

<style lang="scss">
#json {
  text-align: left;
}
</style>
