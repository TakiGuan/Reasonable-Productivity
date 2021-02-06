<!--
 * @Description: Task Vue File
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 21:50:53
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-06 23:09:53
-->
<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>Tasks</h1>
        <v-text-field
          v-model="text"
          label="Enter Task"
          @keypress.enter="addTask"
        ></v-text-field>
        <v-card>
          <v-list dense>
            <v-subheader>Task List</v-subheader>
            <v-list-item-group color="primary">
              <v-list-item v-for="todo in list" :key="todo.text">
                <template #default="{ active }">
                  <v-list-item-action>
                    <v-checkbox :input-value="active"></v-checkbox>
                  </v-list-item-action>

                  <v-list-item-content>
                    <v-list-item-subtitle>
                      {{ todo.text }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  data() {
    return { text: '' }
  },
  computed: {
    ...mapState('tasks', ['list']),
  },
  methods: {
    ...mapMutations('tasks', ['add', 'remove', 'toggle']),
    addTask() {
      this.add(this.text)
      this.text = ''
    },
  },
}
</script>

<style></style>
