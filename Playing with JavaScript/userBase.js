class UserBase {
    constructor(arrayOfNames) {
      this.users = arrayOfNames;
    }
    count() {
      return this.users.length;
    }
    getNames() {
      return this.users.map((user) => user.getName());
    }
    getIntroductions() {
        return this.users.map((user) => user.getIntroduction());
    }
  }

module.exports = UserBase