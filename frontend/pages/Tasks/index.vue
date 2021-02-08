<!--
 * @Description: Task Vue File
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 21:50:53
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-08 23:22:23
-->
<template>
  <v-container>
    <v-row>
      <v-col sm="8" offset-sm="2">
        <v-tabs v-model="tab">
          <v-tab>All</v-tab>
          <v-tab>Next</v-tab>
          <v-tab>Capture</v-tab>
          <v-tab>Projects</v-tab>
          <v-tab>Backlog</v-tab>
        </v-tabs>

        <v-text-field
          placeholder="Search..."
          append-outer-icon="mdi-magnify"
        ></v-text-field>

        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-card class="ma-2">
              <v-card-title>Next Actions</v-card-title>
              <v-card-text>Item No.1</v-card-text>
            </v-card>
            <v-card class="ma-2">
              <v-card-title>Capture</v-card-title>
              <v-card-text>Item No.1</v-card-text>
            </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card>
              <v-list dense>
                <v-subheader>Task List</v-subheader>
                <v-list-item-group color="primary">
                  <v-list-item v-for="(task, i) in tasks" :key="i">
                    <template #default="{ active }">
                      <v-list-item-action>
                        <v-checkbox :input-value="active"></v-checkbox>
                      </v-list-item-action>

                      <v-list-item-content>
                        <span
                          v-if="editingTask.id === task.id"
                          class="d-flex justify-space-between"
                        >
                          <v-text-field
                            v-model="editingTask.title"
                            append-outer-icon="mdi-check"
                            @click:append-outer="saveEdit"
                            @keypress.enter="saveEdit"
                          >
                          </v-text-field>
                          <v-icon @click.stop="cancelEdit"
                            >mdi-close-circle</v-icon
                          >
                        </span>
                        <span v-else class="d-flex justify-space-between">
                          {{ task.title }}

                          <span>
                            <v-icon @click.stop="editTask(i)"
                              >mdi-pencil</v-icon
                            >
                            <v-icon @click.stop="removeTask(task.id)"
                              >mdi-delete-outline</v-icon
                            >
                          </span>
                        </span>
                      </v-list-item-content>
                    </template>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

        <!-- <v-text-field
          v-model="newTask.title"
          label="Enter Task"
          @keypress.enter="addTask"
        ></v-text-field> -->

        <!-- <v-textarea
          v-model="newTask.description"
          label="Description"
          outlined
        /> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      newTask: {
        title: '',
        description: '',
        // TODO
        user: 1,
      },
      editingTask: {},
      tab: null,
    }
  },

  computed: {
    ...mapState('tasks', ['tasks']),
  },
  created() {
    this.getAllTasks()
  },
  methods: {
    // ...mapMutations('tasks', ['add', 'edit', 'remove', 'toggle']),
    ...mapActions('tasks', [
      'getAllTasks',
      'postNewTask',
      'deleteTask',
      'updateTask',
    ]),
    addTask() {
      this.postNewTask(this.newTask)
      this.newTask = {
        title: '',
        description: '',
        // TODO
        user: 1,
      }
    },
    removeTask(taskID) {
      this.deleteTask(taskID)
    },
    editTask(index) {
      this.editingTask = { ...this.tasks[index] }
    },
    cancelEdit() {
      this.editingTask = {}
    },
    saveEdit() {
      const payload = {
        id: this.editingTask.id,
        task: this.editingTask,
      }
      delete payload.task.id

      this.updateTask(payload)
      this.cancelEdit()
    },
  },
}
</script>

<style></style>
