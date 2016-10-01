#ifndef BaseEventReader_H
#define BaseEventReader_H

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"

#include "FWCore/Framework/interface/ConsumesCollector.h"
#include <string>

using namespace std;
//using namespace reco;

template <class G>
class ptSort{
public:
  bool operator()(G o1 ,G o2 ){
    return (o1.pt()>o2.pt());
  }
};
template <class G>
class btagSort{
public:
  btagSort(string Alg): algo(Alg){}
  ~btagSort(){}
  bool operator()(G o1 ,G o2 ){
    return (o1.bDiscriminator(algo)>o2.bDiscriminator(algo));
  }
private:
  string algo;
};

template<typename T >
class BaseEventReader {
public:
  BaseEventReader( edm::ParameterSet const& iPS, edm::ConsumesCollector*  iC){
    token = iC->consumes<T>( iPS.getParameter<edm::InputTag>("Input") );
  }

  virtual double Read( const edm::Event& iEvent ){
    iEvent.getByToken(token, handle);
    return 0.0;
  }
protected :
  edm::Handle<T>  handle; 
  edm::EDGetTokenT< T > token ;
};

#endif
