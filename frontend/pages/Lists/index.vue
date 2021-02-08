<!--
 * @Description: List Index Page
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-08 13:17:46
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-08 15:27:29
-->
<template>
  <v-container>
    <v-row>
      <v-col sm="8" offset-sm="2">
        <v-text-field v-model="newListName">
          <template #append-outer>
            <v-btn color="primary" @click.stop="addList">Add List Item</v-btn>
          </template>
        </v-text-field>
        <v-card>
          <v-treeview :items="lists">
            <template #append="{ item }">
              <v-icon @click.stop="editList(item)">mdi-pencil</v-icon>
              <v-icon @click.stop="removeList(item.id)"
                >mdi-delete-outline
              </v-icon>
            </template>
          </v-treeview>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="editDialog" max-width="300">
      <v-card>
        <v-card-title class="headline"> Edit List Item </v-card-title>
        <v-card-text>
          <v-text-field v-model="selectList.name"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer />

          <v-btn color="green darken-1" text @click="cancelEdit">
            Cancel
          </v-btn>

          <v-btn color="green darken-1" text @click.stop="saveEdit">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      newListName: '',
      selectList: {},
      editDialog: false,
    }
  },
  computed: {
    ...mapState('lists', ['lists']),
  },
  created() {
    this.getAllLists()
  },
  methods: {
    ...mapActions('lists', [
      'getAllLists',
      'postNewList',
      'deleteList',
      'updateList',
    ]),
    addList() {
      const payload = {
        user: 1,
        name: this.newListName,
      }
      this.postNewList(payload)
      // TODO
      this.newListName = ''
    },
    editList(item) {
      this.editDialog = true
      this.selectList = { ...item }
    },
    removeList(listID) {
      this.deleteList(listID)
    },
    cancelEdit() {
      this.editDialog = false
      this.selectList = {}
    },
    saveEdit() {
      const payload = {
        id: this.selectList.id,
        list: this.selectList,
      }
      delete payload.list.id

      this.updateList(payload)
      this.cancelEdit()
    },
  },
}
</script>

<style></style>
