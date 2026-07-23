#include "crow_all.h" // Include the single-header you downloaded

int main() {
    crow::SimpleApp app;

    // Define a simple route
    CROW_ROUTE(app, "/")([](){
        return "Hello world from Crow Single Header!";
    });

    // Set port and run the app
    app.port(18080).multithreaded().run();
}
