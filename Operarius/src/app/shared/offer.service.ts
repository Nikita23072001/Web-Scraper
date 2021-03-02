import { AngularFirestore } from '@angular/fire/firestore';
import { Injectable } from '@angular/core';
import { Offer } from './offer.model';


@Injectable({
  providedIn: 'root'
})

export class OfferService {
  formData: Offer;

  constructor(private firestore: AngularFirestore) {}

  getOffers() {
    return this.firestore.collection('auto').snapshotChanges();
  }
}
