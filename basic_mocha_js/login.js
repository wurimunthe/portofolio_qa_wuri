const request_url = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("API Login", function () { // TES SCENARIO
  it("Verify Success Login with valid email and password", async function () { // TEST CASE
    const response = await request_url // INI BUAT NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") // INI ENDPOINT SETELAH .COM
      .send({ email: "jokotampan900@gmail.com", password: "jokotampan900" }); // INI SESUAI BODY

    expect(response.body.data).to.include('Welcome');
    expect(response.body.status).to.eql('SUCCESS_LOGIN');
    expect(response.body.message).to.eql('Anda Berhasil Login');
  });

it("Verify Failed Login with Invalid email and password", async function () { // TEST CASE
    const response = await request_url // INI BUAT NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") // INI ENDPOINT SETELAH .COM
      .send({ email: "wurimunthe@gmail.com", password: "12345" }); // INI SESUAI BODY

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email atau Password Anda Salah');
    expect(response.body.data).to.eql("User's not found");

  });

it("Verify Failed login with email exceeding the character limit", async function () { // TEST CASE
    const response = await request_url // INI BUAT NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") // INI ENDPOINT SETELAH .COM
      .send({ email: "jokotampan90053443545465765767687gfsdd835466@gmail.com", password: "123454" }); // INI SESUAI BODY  

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Gagal Login');
    expect(response.body.data).to.eql('Email/Password melebihin maksimal karakter');

  });

it("Verify Message Login with password contains with symbols", async function () { // TEST CASE
    const response = await request_url // INI BUAT NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") // INI ENDPOINT SETELAH .COM
      .send({ email: "jokotampan900@gmail.com", password: "123454@!?@****&!" }); // INI SESUAI BODY  

    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Tidak boleh mengandung symbol');
    expect(response.body.data).to.include('Password tidak valid');
  });


});