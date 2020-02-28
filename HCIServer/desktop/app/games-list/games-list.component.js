angular.module('gamesList').component('gamesList', {
    // Note: The URL is relative to our `index.html` file
    templateUrl: 'app/games-list/games-list.template.html',
    controller: function GamesListController($http, $scope) {
        var self = this;
        $http.get('/data?_collection=games').then(function (response) {
            self.list = response.data;
        });

        $scope.orderByMe = function (x) {
            $scope.myOrderBy = x;
        };

        $scope.comments = {};
        $scope.post = function (itemId, currentComment) {
            console.log("index", itemId);
            if (currentComment != '') {
                let itemComments = $scope.comments[itemId];
                if (!itemComments) {
                    itemComments = [];
                }
                itemComments.push(currentComment);
                $scope.comments[itemId] = itemComments;
                self.list[itemId].comments = $scope.comments[itemId];
            }
        }


    }
});