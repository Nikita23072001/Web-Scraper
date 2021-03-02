import { UserProfileComponent } from './user-profile/user-profile.component';
import { SignUpComponent } from './signup/signup.component';
import { AuthGuard } from './shared/guard/auth.guard';
import { SecureInnerPagesGuard } from './shared/guard/secure-inner-pages.guard.ts.guard';
import { VerifyEmailComponent } from './verify-email/verify-email.component';
import { ForgotPasswordComponent } from './forrgot-password/forrgot-password.component';
import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule, CanActivate } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { OffersComponent } from './offers/offers.component';
import { FAQComponent } from './faq/faq.component';
import { OfferComponent } from './offers/offer/offer.component';
import { HowItWorksComponent } from './how-it-works/how-it-works.component';
import { ProfileComponent } from './profile/profile.component';
import { SigninComponent } from './signin/signin.component';
import { ChatComponent } from './chat/chat.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'faq', component: FAQComponent },
  { path: 'sign-in', component: SigninComponent},
  { path: 'offers', component: OffersComponent, canActivate: [AuthGuard] },
  { path: 'new-offer', component:  OfferComponent, canActivate: [AuthGuard] },
  { path: 'profile', component:  ProfileComponent, },
  { path: 'how-it-works', component: HowItWorksComponent },
  { path: 'register-user', component: SignUpComponent},
{ path: 'forgot-password', component: ForgotPasswordComponent },
{ path: 'verify-email-address', component: VerifyEmailComponent },
{ path: 'user-profile', component: UserProfileComponent },
{ path: 'chat', component: ChatComponent }


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
