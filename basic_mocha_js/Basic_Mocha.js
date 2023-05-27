mocha.setup('bdd');
var expect = chai.expect;

// Silakan tambah function describe lain atau langsung tambahkan it didalam describe dibawah ini, tambahkan 3 it untuk membandingkan 3 value
// silakan belajar tipe data js disini https://www.w3schools.com/js/js_datatypes.asp
// silakan copas seluruh code disini dan uji code kalian ke https://codepen.io/barruawd/pen/WNyNrbp

// to.deep.equal, untuk membandingkan 2 Object/List
// to.equal, untuk membandingkan 2 Value Sama 
// not.to.equal, untuk membandingkan 2 Value Berbeda 

describe('Belajar Membandingkan 2 Value', function() {
  it('Verify 2 Value is equal', function() {
    expect('Jago QA').to.equal('Jago QA');
  });
  it('Verify 2 Numbers (Integer vs Integer) is equal', function() {
    expect(102).to.equal(102);
  });
  it('Verify 2 Object is equal', function() {
    expect({'nama':'Jago QA'}).to.deep.equal({'nama':'Jago QA'});
  });
  it('Verify 2 Value is not equal', function() {
    expect('Jago qa').not.to.equal('Jago QA');
  });
 it('Validate 2 list is equal', function() {
    expect('apel,pisang,anggur').to.deep.equal('apel,pisang,anggur');
  }); 
  it('Validate 2 Object (String vs String) is equal', function() {
    expect('panda').to.equal('panda');
  });
  
  it('Validate 2 list is not equal', function() {
    expect('apel,pisang,anggur').not.to.equal('apel,pisang,salak');
  });
  
});
mocha.run();