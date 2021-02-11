<!--
 * @Description: Task Vue File
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 21:50:53
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-11 16:10:49
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
          v-model="searchValue"
          placeholder="Search..."
          append-outer-icon="mdi-magnify"
        ></v-text-field>

        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-row class="ma-1 d-flex flex-wrap">
              <v-card class="ma-2" width="240px">
                <v-card-title>
                  <v-btn text @click="tab = 1"> Next Actions </v-btn>
                </v-card-title>
                <v-card-text>Item No.1</v-card-text>
              </v-card>
              <v-card class="ma-2" width="240px">
                <v-card-title>
                  <v-btn text @click="tab = 2"> Capture </v-btn>
                </v-card-title>
                <v-card-text>Item No.1</v-card-text>
              </v-card>
            </v-row>
          </v-tab-item>
          <v-tab-item>
            <v-card v-if="newTask.show" outlined>
              <v-card-text>
                <v-text-field
                  ref="newTaskTitle"
                  v-model="newTask.title"
                  label="Title"
                  outlined
                ></v-text-field>

                <v-textarea
                  v-model="newTask.description"
                  label="Description"
                  outlined
                />
              </v-card-text>
              <v-card-actions>
                <v-btn color="success" @click="addTask">Save</v-btn>
                <v-btn color="secondary" @click="toggleNewTask">Cancel</v-btn>
              </v-card-actions>
            </v-card>
            <v-card>
              <v-list dense>
                <v-list-item-group color="primary">
                  <v-list-item v-for="(task, i) in tasks" :key="i">
                    <template #default>
                      <v-list-item-action>
                        <v-checkbox
                          :input-value="task.completed"
                          @click.stop="toggleChecked(task)"
                        ></v-checkbox>
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
                          <span
                            :class="{
                              'text--disabled text-decoration-line-through':
                                task.completed,
                            }"
                          >
                            {{ task.title }}
                          </span>

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

        <v-btn
          class="mx-2 float-right"
          fab
          color="primary"
          @click.stop="toggleNewTask"
        >
          <v-icon dark> mdi-plus </v-icon>
        </v-btn>
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
        show: false,
        title: '',
        description: '',
        // TODO
        user: 1,
      },
      searchValue: '',
      editingTask: {},
      tab: 1,
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
    toggleNewTask() {
      this.newTask.show = !this.newTask.show
      if (this.newTask.show) {
        this.$nextTick(() => {
          this.$refs.newTaskTitle.focus()
        })
      }
    },
    addTask() {
      this.postNewTask(this.newTask)
      this.newTask = {
        show: false,
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
    toggleChecked(task) {
      const payload = {
        id: task.id,
        task: {
          completed: !task.completed,
        },
      }
      this.updateTask(payload)
    },
  },
}
</script>

<style></style>
