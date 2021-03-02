import { AngularFirestore } from '@angular/fire/firestore';
import { Component, OnInit } from '@angular/core';
import { OfferService } from 'src/app/shared/offer.service';
import { NgForm } from '@angular/forms';
import * as firebase from 'firebase';
import { NgModule } from '@angular/core';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-offer',
  templateUrl: './offer.component.html',
  styleUrls: ['./offer.component.css']
})
export class OfferComponent implements OnInit {


  constructor( public service: OfferService,  private firestore: AngularFirestore, private toastr: ToastrService) {}

  ngOnInit() {
    this.resetForm();
  }

  resetForm(form?: NgForm) {
    if (form != null) {
    form.resetForm();
    }
    this.service.formData = {
      id: null,
      title: '',
      content: '',
      location: '',
    };
  }

  onSubmit(form: NgForm) {
    const data = form.value;
    this.firestore.collection('auto').add(data);
    this.resetForm(form);
    this.toastr.success('Submitted successfully', 'Offer registerd');
  }

}
